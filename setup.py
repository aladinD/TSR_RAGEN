from setuptools import find_namespace_packages, setup


CORE_DEPENDENCIES = [
    "accelerate",
    "anthropic",
    "codetiming",
    "datasets",
    "dill",
    "flash-attn==2.7.4.post1",
    "gym",
    "gym_sokoban",
    "gymnasium[toy-text]",
    "hydra-core",
    "matplotlib",
    "numpy",
    "openai",
    "pandas",
    "peft",
    "Pillow",
    "pyarrow>=15.0.0",
    "pylatexenc",
    "pytest",
    "ray>=2.10",
    "tensordict>=0.8.0,<0.9.0",
    "together",
    "torchdata",
    "transformers",
    "vllm==0.8.2",
    "wandb",
]

WEBSHOP_DEPENDENCIES = [
    "beautifulsoup4",
    "cleantext",
    "faiss-cpu==1.11.0",
    "flask",
    "gdown",
    "html2text",
    "pyserini",
    "rank_bm25",
    "rich",
    "spacy",
    "thefuzz",
]

setup(
    name="tsr-ragen",
    version="0.1.0",
    description="Multi-turn reinforcement learning for language-model agents",
    packages=find_namespace_packages(include=["ragen", "ragen.*"]),
    install_requires=CORE_DEPENDENCIES,
    extras_require={"webshop": WEBSHOP_DEPENDENCIES},
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
    ],
)
