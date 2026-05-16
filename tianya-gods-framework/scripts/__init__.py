"""
天涯神贴大神智囊团 - 多Agent决策系统
基于ClawTeam架构实现20位大神的并行决策

使用示例:
    from scripts.team_orchestrator import TianyaGodsTeam
    import asyncio
    
    async def main():
        team = TianyaGodsTeam()
        result = await team.analyze("我现在该不该买房？")
        print(result)
    
    asyncio.run(main())
"""

__version__ = "3.0.0"
__author__ = "女娲 · Skill造人术"
__license__ = "MIT"

from .team_orchestrator import TianyaGodsTeam, GodProfile, AnalysisResult

__all__ = [
    "TianyaGodsTeam",
    "GodProfile", 
    "AnalysisResult",
]
