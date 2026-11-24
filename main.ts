// Entry program for the 24 November 2026 news-image bounty.
//
// The front page is already drawn and stored beside this file as
// entry.png. This program's only job is to place an exact copy of
// that image where the grader expects it, so both runs of the
// program produce byte-identical output.
//
// It uses only the Node standard library: the file system helpers
// and the path helper. No network, no extra packages.
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

// Node runs this file as an ES module, where __dirname does not
// exist, so derive the entry's own folder from its module URL.
const here = dirname(fileURLToPath(import.meta.url));

// The grader sets MAKEFUN_OUTPUT_DIR; fall back to /output, the
// directory the bounty rules name, when it is not set.
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const sourceImage = join(here, "entry.png");
const targetImage = join(outputDir, "entry.png");

// Make sure the destination folder exists before writing into it.
if (!existsSync(outputDir)) {
  mkdirSync(outputDir, { recursive: true });
}

// Fail loudly, instead of writing an empty or partial file, if the
// finished front page is not sitting beside this program.
if (!existsSync(sourceImage)) {
  throw new Error(`missing entry image: ${sourceImage}`);
}

// Read the finished front page into memory, then write those exact
// bytes out again. Reading and writing the raw buffer (rather than
// re-encoding anything) keeps the two runs byte-identical.
const imageBytes = readFileSync(sourceImage);
writeFileSync(targetImage, imageBytes);

console.log(`wrote ${targetImage} (${imageBytes.length} bytes)`);
