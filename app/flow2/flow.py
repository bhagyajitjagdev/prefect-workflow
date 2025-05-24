"""
Flow 2 - Another Pipeline Flow
Steps: Step A → Step B → Step C
"""

from typing import Any, Dict

from prefect import flow, get_run_logger

from app.flow2.tasks import step_a, step_b, step_c


@flow(
    name="flow2-another-pipeline",
    description="Flow 2: Another pipeline with Step A, Step B, Step C",
    persist_result=True,
    retries=1,
)
def another_pipeline_flow(message: str = "Default message") -> Dict[str, Any]:
    """
    Flow 2: Another sequential pipeline

    Args:
        message: Input message to process

    Returns:
        Final analysis result
    """
    logger = get_run_logger()

    logger.info("🚀 Starting Flow 2 - Another Pipeline")
    logger.info("=" * 50)

    try:
        # Execute Step A
        logger.info("📍 Executing Step A...")
        step_a_result = step_a(message)

        # Execute Step B (depends on Step A)
        logger.info("📍 Executing Step B...")
        step_b_result = step_b(step_a_result)

        # Execute Step C (depends on both Step A and Step B)
        logger.info("📍 Executing Step C...")
        step_c_result = step_c(step_a_result, step_b_result)

        # Flow summary
        flow_summary = {
            "flow_name": "Flow 2 - Another Pipeline",
            "status": "success",
            "total_steps": 3,
            "step_a_result": step_a_result,
            "step_b_result": step_b_result,
            "step_c_result": step_c_result,
            "final_message": step_c_result["message"],
        }

        logger.info("=" * 50)
        logger.info("🎉 Flow 2 completed successfully!")
        logger.info(f"📋 Flow Summary: {flow_summary['final_message']}")

        return flow_summary

    except Exception as e:
        logger.error("❌ Flow 2 failed!")
        logger.error(f"Error: {str(e)}")
        raise


if __name__ == "__main__":
    # For local testing
    result = another_pipeline_flow("Test message")
    print("Flow 2 Result:", result)
