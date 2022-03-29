// ---------------------------------------------------------------------------
// Usage:
//
//      npm run vss
// ---------------------------------------------------------------------------

import fs from 'fs'
import log from 'ololog'
import ansi from 'ansicolor'
import { execSync } from 'child_process'
import { copyFile } from './fsLocal.js'
import { pathToFileURL } from 'url'
import packageJson from '../package.json' assert { type: "json" };

ansi.nice

//-----------------------------------------------------------------------------

function vss (filename, template, version) {
    log.bright.cyan ('Single-sourcing version', version, './package.json → ' + filename.yellow)
    const content = fs.readFileSync (filename, 'utf8')
    const regexp  = new RegExp (template.replace (/[-\/\\^$*+?.()|[\]{}]/g, '\\$&') // escape string for use in regexp
                                        .replace ('\\{version\\}', '\\d+\\.\\d+\\.\\d+'), 'g')
    fs.truncateSync  (filename)
    fs.writeFileSync (filename, content.replace (regexp, template.replace ('{version}', version)))
}

// ----------------------------------------------------------------------------

async function vssEverything () {

    const version = packageJson['version']

    log.bright ('New version: '.cyan, version)

    vss ('./ccxt.js',                                    "const version = '{version}'", version)
    vss ('./php/Exchange.php',                           "$version = '{version}'",      version)
    vss ('./php/async/Exchange.php',                     "VERSION = '{version}'",       version)
    vss ('./php/async/Exchange.php',                     "$version = '{version}'",      version)
    vss ('./php/Exchange.php',                           "VERSION = '{version}'",       version)
    vss ('./python/ccxt/__init__.py',                    "__version__ = '{version}'",   version)
    vss ('./python/ccxt/base/exchange.py',               "__version__ = '{version}'",   version)
    vss ('./python/ccxt/async_support/__init__.py',      "__version__ = '{version}'",   version)
    vss ('./python/ccxt/async_support/base/exchange.py', "__version__ = '{version}'",   version)

    vss ('./README.md',       "ccxt@{version}", version)
    vss ('./wiki/Install.md', "ccxt@{version}", version)

    const pythonFiles = [
        'package.json',
        'LICENSE.txt',
        'keys.json',
        'README.md',
    ]

    pythonFiles.forEach ((fileName) => copyFile ('./' + fileName, './python/' + fileName))

    log.bright.green ('Version single-sourced successfully.')
}

// ============================================================================
// main entry point
let metaUrl = import.meta.url
metaUrl = metaUrl.substring(0, metaUrl.lastIndexOf(".")) // remove extension
const url = pathToFileURL(process.argv[1]);
if (metaUrl === url.href) {

    // if called directly like `node module`

    await vssEverything ()

} else {

    // do nothing if required as a module
}

// ============================================================================

export {
    vss,
    vssEverything,
}
