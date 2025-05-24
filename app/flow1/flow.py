"""
Flow 1 - Simple Pipeline Flow
Steps: Step 1 → Step 2 → Step 3
"""

from typing import Any, Dict

from prefect import flow, get_run_logger

from app.flow1.tasks import step_1, step_2, step_3


@flow(
    name="flow1-simple-pipeline",
    description="Flow 1: Simple pipeline with Step 1, Step 2, Step 3",
    persist_result=True,
    retries=1,
)
def simple_pipeline_flow(message: str = "Default message") -> Dict[str, Any]:
    """
    Flow 1: Simple sequential pipeline

    Args:
        message: Input message to process

    Returns:
        Final processing result
    """
    logger = get_run_logger()

    logger.info("🚀 Starting Flow 1 - Simple Pipeline")
    logger.info("=" * 50)

    try:
        # Execute Step 1
        logger.info("📍 Executing Step 1...")
        step1_result = step_1(message)

        # Execute Step 2 (depends on Step 1)
        logger.info("📍 Executing Step 2...")
        step2_result = step_2(step1_result)

        # Execute Step 3 (depends on both Step 1 and Step 2)
        logger.info("📍 Executing Step 3...")
        step3_result = step_3(step1_result, step2_result)

        # Flow summary
        flow_summary = {
            "flow_name": "Flow 1 - Simple Pipeline",
            "status": "success",
            "total_steps": 3,
            "step1_result": step1_result,
            "step2_result": step2_result,
            "step3_result": step3_result,
            "final_message": step3_result["message"],
        }

        logger.info("=" * 50)
        logger.info("🎉 Flow 1 completed successfully!")
        logger.info(f"📋 Flow Summary: {flow_summary['final_message']}")

        return flow_summary

    except Exception as e:
        logger.error("❌ Flow 1 failed!")
        logger.error(f"Error: {str(e)}")
        raise


if __name__ == "__main__":
    # For local testing
    result = simple_pipeline_flow("Test message")
    print("Flow 1 Result:", result)
