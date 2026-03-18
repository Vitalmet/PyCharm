'''import asyncio


async def download_file(file_id: int) -> None:
    print(f'Начало скачивания {file_id}')
    await asyncio.sleep(1, 3)
    print(f'Скачивание {file_id} завершено.')

async def process_file(file_id: int) -> None:
    print(f'Идет обработка {file_id}')
    await asyncio.sleep(1, 2)
    print(f'Обработка{file_id} завершена.')

async def main() -> None:
    for file_id in range(1, 4):
        await download_file(file_id)
        await process_file(file_id)

if __name__ == '__main__':
    asyncio.run(main())'''

'''import asyncio
from dataclasses import dataclass
from typing import List


@dataclass
class Source:
    slug: str
    delay: float
    should_fail: bool = False


async def fetch_report(source: Source) -> str:
    print(f"Начало {source.slug}")
    await asyncio.sleep(source.delay)
    if source.should_fail:
        raise RuntimeError(f"{source.slug} недоступен")
    print(f"Готово {source.slug}")
    return f"{source.slug}:ok"


async def collect_reports(sources: List[Source]) -> List[str]:
    results: List[str] = []
    failed = False

    async def runner(source: Source) -> None:
        report = await fetch_report(source)
        results.append(report)

    try:
        async with asyncio.TaskGroup() as tg:
            for source in sources:
                tg.create_task(runner(source))
    except* RuntimeError as eg:
        for err in eg.exceptions:
            print(err)
        failed = True
    finally:
        print("Сбор завершён")

    if failed:
        return ["reports failed"]
    return results


async def main() -> None:
    sources = [
        Source("metrics", 0.5),
        Source("logs", 0.8),
        Source("billing", 0.2, should_fail=True),
    ]
    print(await collect_reports(sources))


if __name__ == "__main__":
    asyncio.run(main())'''

