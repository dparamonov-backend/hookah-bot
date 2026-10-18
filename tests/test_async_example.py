import pytest
async def mock_async_function(value: int) -> int:
    return value*2
@pytest.mark.asyncio
async def test_async_function() -> None:
    assert await mock_async_function(1) == 2
