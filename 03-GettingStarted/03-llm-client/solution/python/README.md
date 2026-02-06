# Running this sample

You're recommended to install `uv` but it's not a must, see [instructions](https://docs.astral.sh/uv/#highlights)

## -0- GITHUB Token must have Models *User* Permission

## -1- Create a virtual environment

```bash
python3 -m venv venv
```

## -2- Activate the virtual environment

```bash
source venv/bin/activate
```

## -3- Install the dependencies

```bash
pip3 install "mcp[cli]"
pip3 install openai
pip3 install azure-ai-inference
```

## -4- Run the sample


```bash
python3 client.py
```

You should see an output similar to:

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
                    INFO     Processing request of type ListToolsRequest                                                                               server.py:534
LISTING TOOLS
Tool:  add
Tool {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}
CALLING LLM
TOOL:  {'function': {'arguments': '{"a":2,"b":20}', 'name': 'add'}, 'id': 'call_BCbyoCcMgq0jDwR8AuAF9QY3', 'type': 'function'}
[05/08/25 21:04:55] INFO     Processing request of type CallToolRequest                                                                                server.py:534
TOOLS result:  [TextContent(type='text', text='22', annotations=None)]
```
