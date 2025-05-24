# Prefect Workflow

This is a simple workflow using Prefect. It consists of two flows:

1. Flow 1 - Simple Pipeline
2. Flow 2 - Another Pipeline

## Flow 1 - Simple Pipeline

Flow 1 is a simple sequential pipeline with three steps:

1. Step 1 - Initial processing
2. Step 2 - Processing step 1 results
3. Step 3 - Final processing with results from both previous steps

## Flow 2 - Another Pipeline

Flow 2 is a more complex pipeline with four steps:

1. Step A - Initial processing
2. Step B - Processing step A results
3. Step C - Final processing with results from both previous steps

## Setup

1. Clone the repository:

```bash
git clone https://github.com/bhagyajitjagdev/prefect-workflow.git
```

2. Navigate to the project directory:

```bash
cd prefect-workflow
```

3. Run the docker compose file to start the Prefect server and workers:

```bash
docker compose up -d
```

4. Wait for the Prefect server to start. You can check the status by running:

```bash
docker compose ps
```

5. Once the server is up, you can deploy the flows to the workers:

```bash
docker exec prefect-worker-1 prefect deploy --all
```

6. You can now access the Prefect UI at http://localhost:4200

7. To Start the flows, you can run go to the Prefect UI and click on the "Flows" tab. From there, you can start the flows by clicking on the "Start" button next to each flow.

8. You can setup a schedule for the flows to run automatically. To do this, go to the prefect.yaml file and add a schedule for the flows.

# Local Testing

If you want to test the flows locally, you can run each flow individually. To do this, you can use the following commands:

## Setup UV:

1. [Install UV](https://docs.astral.sh/uv/getting-started/installation/)

2. Run the following command to install the dependencies:

```bash
uv sync
```

## Run Flows

```bash
# Run Flow 1 - Simple Pipeline
python -m app.flow1.flow

# Run Flow 2 - Another Pipeline
python -m app.flow2.flow
```

---
