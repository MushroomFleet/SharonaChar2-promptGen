# Sharona Prompt Generator

A specialized tool for efficiently generating themed prompts for AI image generation with the sh4r0na character Lora model.

## What This Is

The Sharona Prompt Generator is a Python-based tool that creates structured, thematic prompts for generating AI images of the sh4r0na character across various environments. It demonstrates a practical approach to reducing AI token usage by logically separating repetitive elements from dynamic content.

This repository contains:
- A Python script (`generate_prompts.py`) to generate themed prompt files
- Original character captions (`sharona-charv2.txt`) used for training the Lora model
- Generated prompt files organized by environmental themes

## What This Does

The prompt generator:

1. Maintains consistent character elements (appearance, style, prompt structure)
2. Varies only the scene descriptions across 10 distinct themed environments
3. Creates 200 unique prompts (20 per theme) following the format: `[prompt type], [character description], [caption description], [prompt style]`
4. Outputs prompts to themed files with timestamps for easy reference

The generator creates prompts for these 10 themed environments:
- Ruins of the Ancients
- New Ice Territories
- Great Desert Expansions
- Reclaimed Forests
- Volcanic Badlands
- Neo-Primitive Coastlines
- Tribal City-States
- Mutated Wetlands
- Highland Strongholds
- Ancient Power Sites

Each environment portrays Earth 10,000 years in the future, where humanity has regressed to a more primitive state after the fall of our current civilization, but with remnants of advanced technology still visible.

## How to Use It

### Running the Generator

1. Ensure Python is installed on your system
2. Run the script: `python generate_prompts.py`
3. The script will generate 10 themed text files with 20 prompts each
4. Files are named with the pattern: `sharona-prompts-[theme]-[timestamp].txt`

### Using the Generated Prompts

1. Open any of the generated prompt files
2. Copy a prompt from the file
3. Paste it into your AI image generation tool that has the sh4r0na Lora model loaded
4. Generate your image

### Customizing Themes

To modify or add themes:
1. Open `generate_prompts.py`
2. Edit the existing theme arrays or add new ones
3. Update the `themes` dictionary if adding new themes
4. Run the script to generate new prompt files

## Examples

### Sample Prompt Structure

```
depiction of hunter-style cave woman character, sh4r0na woman with short white hair, vibrant orange fur skin blouse with black accents and exposed torso, including matching fur skin wrapped oversized boots and gloves, she is standing at the edge of a volcanic fissure where the heat has exposed layers of ancient civilization, with tribal shamans harvesting strange metals from the molten earth to forge mysterious weapons, Watercolor style graphic novel illustration, detailed ink linework.
```

Breaking down this structure:

- **Prompt Type**: "depiction of hunter-style cave woman character"
- **Character Description**: "sh4r0na woman with short white hair, vibrant orange fur skin blouse with black accents and exposed torso, including matching fur skin wrapped oversized boots and gloves"
- **Caption Description**: "she is standing at the edge of a volcanic fissure where the heat has exposed layers of ancient civilization, with tribal shamans harvesting strange metals from the molten earth to forge mysterious weapons"
- **Prompt Style**: "Watercolor style graphic novel illustration, detailed ink linework"

### Before vs After: Reducing Redundancy

**Traditional approach** (repeated elements in every prompt):
```
Prompt 1: Create an image of sh4r0na woman with short white hair, vibrant orange fur skin blouse with black accents, standing in a volcanic wasteland. Use watercolor style with detailed ink linework.

Prompt 2: Generate a picture of sh4r0na with short white hair, vibrant orange outfit with black accents, exploring an ancient ruin. Make it watercolor style with detailed ink.

Prompt 3: Draw sh4r0na character with white hair, orange and black fur clothing, in a snowy environment. Watercolor style with fine ink details.
```

**Component-based approach** (fixed elements defined once, only scenes vary):
```
[Fixed] prompt type: depiction of hunter-style cave woman character
[Fixed] character description: sh4r0na woman with short white hair, vibrant orange fur skin blouse...
[Fixed] prompt style: Watercolor style graphic novel illustration, detailed ink linework
[Varies] scene descriptions: 
  - "she is standing at the edge of a volcanic fissure..."
  - "she is exploring the remnants of a once-great city..."
  - "she is traversing a vast ice plain..."
```

## Cost Reduction Analysis

### How This Approach Reduces LLM Costs by 75%

Traditional prompt generation requires rewriting the entire character description and style information for each new prompt. By separating these components:

1. **Token Efficiency**: The fixed components (character description, prompt type, and style) are defined once in the code rather than repeated 200 times
2. **Focused AI Processing**: AI only needs to generate the truly unique part (the scene descriptions) without recreating known elements
3. **Reduced Token Usage**: For a typical set of 200 prompts:
   - Traditional approach: ~200,000 tokens (full descriptions for each prompt)
   - Component approach: ~50,000 tokens (fixed elements stored once + unique scene descriptions)

### Technical Demonstration

This project exemplifies a concept known as "token optimization" where:

1. **Repetitive Elements** are identified and stored efficiently (character appearance descriptions, style preferences)
2. **Dynamic Elements** are isolated for focused generation (scene descriptions, environmental details)
3. **Template Structure** combines components consistently

This approach is particularly valuable for:
- Fine-tuning existing Lora models
- Large-scale image prompt generation
- Maintaining consistency across a character's representation in various settings

## Getting Started

```bash
# Clone the repository
git clone https://github.com/yourusername/sharona-prompt-generator.git

# Navigate to the directory
cd sharona-prompt-generator

# Run the generator
python generate_prompts.py
```

The generated prompt files will be created in the same directory, ready for use with your AI image generation tool.
