# mama-ai Architecture (Prototype v1.1)

- `src/simple_cli.py` – minimal CLI entrypoint
- `src/api.py` – FastAPI service with `/health` and `/predict`
- `src/ui_demo.py` – Streamlit-based hackathon demo
- `models/` – place for model weights or checkpoints
- `data/` – sample datasets or input/output artifacts

mama-ai/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── ui/
│   ├── high_fidelity/
│   │   ├── 01_welcome.png      (placeholder)
│   │   ├── 02_capture.png      (placeholder)
│   │   ├── 03_meal_analysis.png (placeholder)
│   │   ├── 04_activity_input.png (placeholder)
│   │   ├── 05_emotion_input.png (placeholder)
│   │   ├── 06_final_response.png (placeholder)
│   │   └── 07_weekly_view.png (placeholder)
│   │
│   └── wireframes/
│       ├── flow_diagram.drawio
│       └── layout_grid.png
│
├── model/
│   ├── prompts/
│   │   ├── prompt_meal_analysis.md
│   │   ├── prompt_emotion_analysis.md
│   │   ├── prompt_grocery_list.md
│   │   ├── prompt_food_swap.md
│   │   └── prompt_tone_evaluation.md
│   │
│   └── pipeline.ipynb
│
├── demo/
│   ├── input_sample/
│   │   ├── meal_sample_01.jpg (placeholder)
│   │   └── meal_sample_02.jpg (placeholder)
│   │
│   ├── expected_outputs/
│   │   ├── response_example_01.json
│   │   └── response_example_02.json
│   │
│   └── demo_flow_script.txt
│
└── docs/
    ├── brand_guidelines.pdf      (placeholder text)
    ├── storyboard_30s_pitch.pdf  (placeholder text)
    └── pitch_slides_5pages.pdf   (placeholder text)
