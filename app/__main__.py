from uvicorn import run

from app.api import app

def main():
	# Run the FastAPI app with uvicorn when executing the package: python -m app
	run(app, host="127.0.0.1", port=8000, log_level="info")


if __name__ == "__main__":
	main()

