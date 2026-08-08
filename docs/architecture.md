# System Architecture & Agent Integration 📐

```
[ User Request ] ---> [ Agent Host (Cursor / Claude Code / Antigravity) ]
                                      |
                     [ Target SKILL.md Protocol Loader ]
                                      |
       +------------------------------+------------------------------+
       |                              |                              |
[ Python / R Script Execution ] [ REST API Query (VEP/PubMed) ] [ Nextflow Cloud Dispatch ]
```
