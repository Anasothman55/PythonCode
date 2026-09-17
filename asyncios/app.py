import asyncio
import time


def sync_function(test_param: str) -> str:
  print("This is a synchronous function.")
  time.sleep(0.1)
  return f"Sync Result: {test_param}"


# ALSO KNOWN AS A COROUTINE FUNCTION
async def async_function(test_param: str) -> str:
  print("This is an asynchronous coroutine function.")
  await asyncio.sleep(0.1)
  return f"Async Result: {test_param}"



async def main():

  # loop = asyncio.get_running_loop()
  # future = loop.create_future()
  # print("Waiting for the future to be set...")

  # future.set_result("Future is set!")
  # result = await future 
  # print(result)

  # coroutin_obj = async_function("Hello")
  # print(coroutin_obj)

  # coroutine_result = await coroutin_obj
  # print(coroutine_result)


  task = asyncio.create_task(async_function("Hello"))
  print(task)

  task_result = await task
  print(task_result)



if __name__ == "__main__":
  asyncio.run(main())

