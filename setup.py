from setuptools import setup, find_packages

setup(
    name="personal-finance-dashboard",
    version="1.0.0",
    description="A personal finance dashboard with expense tracking, visualization, and real-time data integration.",
    author="Michael Porter",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "matplotlib",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "finance-dashboard=expense_tracker:main"
        ]
    }
)
