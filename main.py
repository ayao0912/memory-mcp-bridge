from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP(name="gemini-memories")

@mcp.tool()
async def search_memory(query: str, count: int = 5) -> str:
    """搜索Gemini和瑶瑶的共同记忆。当瑶瑶说"你记得""以前""上次"时使用。"""
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            f"https://memory-sync.zeabur.app/mcp/search_memory",
            params={"q": query, "count": count}
        )
        return resp.text

if __name__ == "__main__":
    mcp.run(transport="sse")
