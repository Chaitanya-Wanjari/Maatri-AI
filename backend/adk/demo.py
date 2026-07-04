from backend.adk.agents import root_agent

print("=" * 60)
print("MAATRI ADK AGENT")
print("=" * 60)

print(root_agent)

print("\nSub Agents:\n")

for agent in root_agent.sub_agents:
    print("-", agent.name)