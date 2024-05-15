## Autogen


### Basic of AutoGen

- [official docs that to simplify the Agent creation and interactive](https://microsoft.github.io/autogen/docs/Getting-Started)
  
  In summary:
    - Create a framework that could create various agents and each of them could interactive with each other.
    - A default prompt that will be used to guide agent what to do, like solve problem with current support functions, register some functions
    - A diverse of type to create agents that could interactive: 2-agents, groups, sequential agents etc.
    - Recommend model is GPT4
    - A list of tools that is predefined in python code
    - Run the created python or shell code in local server, or in docker, or jupyter that could do memory of previous codes 
    - Max run of the agent could be configured: max_times, keyword in respones like terminate.