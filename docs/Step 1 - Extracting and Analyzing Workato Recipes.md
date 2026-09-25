# Step 1: Extracting and Analyzing Workato Recipes

## What we did

Before writing a single line of n8n, we needed to understand what each Workato recipe actually does. To do that, we followed a simple 3-step process for every recipe:

1. **Extract the recipe as JSON**
2. **Clean up the JSON**
3. **Generate a plain-English `.md` document explaining the pipeline**

## 1. Extracting the JSON from Workato

Workato doesn't give you a simple "export to JSON" button for a recipe. Instead, we used the **"Inspect"** option inside the Workato recipe editor, which shows the recipe's internal representation. We copied that output and saved it as a `.json` file per recipe, inside the `recipes/` folder.

Example: `recipes/NS & NF Automation - Callable - Create Customer in Netsuite.json`

## 2. Cleaning up the JSON

The JSON we got from "Inspect" was **stringified**: instead of a normal JSON object, the whole recipe (and some fields inside it) came wrapped as escaped text, e.g. `"result": "{\"number\":0, ... }"`. That's hard to read and impossible to search.

To fix this, we used a small script — [`scripts/clean_recipe_json.py`](../scripts/clean_recipe_json.py) — that goes through the file and un-escapes/parses any text that is actually JSON, turning it back into a real, nested, readable JSON object. We ran it once per recipe file:

```bash
python3 scripts/clean_recipe_json.py "recipes/My Recipe.json"
```

After this, every recipe file became a clean, properly nested JSON document that we (and any tool) can read and search normally.

## 3. Generating the plain-English `.md` documentation

Once the JSON was clean, we read through it recipe by recipe and wrote a companion `.md` file (same name as the JSON) describing the pipeline in plain English, so that anyone (technical or not) can understand what the recipe does without reading Workato's internal JSON.

Each `.md` file follows the same structure:

- **Recipe Overview**: a short paragraph explaining the purpose of the recipe, plus a simplified **Mermaid diagram** showing the flow at a glance (steps as boxes/names, not technical details).
- **Steps**: a breakdown of every step in the recipe, each one with:
  - **Name** — what the step is called.
  - **Logic** — what it actually does, in plain language.
  - **Inputs** — what data it needs.
  - **Outputs** — what data it produces.
  - **Step Number / Previous Step Number / Next Step Number** — so the flow (including branches like if/else, try/catch, loops) can be followed easily.
- **Key Business Logic Notes** (when relevant): important quirks, edge cases, or bugs found in the original Workato recipe that are worth knowing about before/while migrating to n8n.

## Result

For each Workato recipe we now have:
- A clean `.json` file with the full recipe logic (trigger, steps, conditions, lookups, etc.) in normal JSON format.
- A clean `.md` file explaining, in plain English, what the recipe does and how it flows step by step.

This documentation is what we'll use as the source of truth when rebuilding each recipe as an n8n workflow.
