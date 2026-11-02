import { readFile, mkdtemp, rm, access } from 'node:fs/promises'
import { spawnSync } from 'node:child_process'
import { tmpdir } from 'node:os'
import { join, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'
import { transformWithEsbuild } from 'vite'

const root = fileURLToPath(new URL('../../', import.meta.url))
const localPython = join(root, '.venv-pdf', process.platform === 'win32' ? 'Scripts/python.exe' : 'bin/python')
let python = process.env.PDF_PYTHON
if (!python) {
  try { await access(localPython); python = localPython } catch { python = process.platform === 'win32' ? 'python' : 'python3' }
}
const data = {}
for (const locale of ['fr', 'en']) {
  const filename = join(root, `src/i18n/${locale}.ts`)
  const { code } = await transformWithEsbuild(await readFile(filename, 'utf8'), filename)
  data[locale] = (await import(`data:text/javascript;base64,${Buffer.from(code).toString('base64')}`)).default
}
const temp = await mkdtemp(join(tmpdir(), 'cv-pdf-'))
try {
  const result = spawnSync(python, [join(root, 'scripts/pdf/render.py'), root, temp, resolve(root, 'public')], {
    input: JSON.stringify(data), encoding: 'utf8', stdio: ['pipe', 'inherit', 'inherit']
  })
  if (result.error) console.error('Python introuvable. Installer Python 3 puis lancer npm run pdf:setup.', result.error.message)
  process.exitCode = result.status ?? 1
} finally { await rm(temp, { recursive: true, force: true }) }
