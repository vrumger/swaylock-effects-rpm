import { readFile, writeFile } from 'node:fs/promises';

const request = await fetch(
    'https://api.github.com/repos/jirutka/swaylock-effects/tags',
);
const [tag] = await request.json();
const spec = await readFile('swaylock-effects.spec', 'utf-8');

const latestVersion = tag.name.replace(/^v/, '');
const currentVersion = spec.match(/^%define upstreamversion (.+)$/m)[1];

if (latestVersion === currentVersion) {
    console.log('no new version available');
    process.exit(0);
}

const newSpec = spec.replace(
    /^%define upstreamversion .+$/m,
    `%define upstreamversion ${latestVersion}`,
);

await writeFile('swaylock-effects.spec', newSpec);
