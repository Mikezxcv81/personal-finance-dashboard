from setuptools import setup, find_packages

setup(
    name="personal-finance-dashboard",
    version="1.0.0",
    description="A personal finance dashboard with expense tracking and visualization.",
    author="Your Name",
    packages=find_packages(where="src"),  # Specify 'src' as the base directory
    package_dir={"": "src"},              # Map the root to 'src'
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

