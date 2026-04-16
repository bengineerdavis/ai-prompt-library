# Architecture

The structural models for libraries, projects, workspaces, and the build pipeline.

| File                                   | Contents                                                    |
| -------------------------------------- | ----------------------------------------------------------- |
| [library-model.md](./library-model.md) | Library, collection, and prompt directory contract          |
| [project-model.md](./project-model.md) | Project, workspace, environment, and config layout          |
| [pipeline.md](./pipeline.md)           | Internal Build → Specializer → Optimizer → Profile pipeline |

For the scoring and threshold model that the pipeline uses, see
[`../internals/`](../internals/README.md).
