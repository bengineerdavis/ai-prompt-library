# Lexicon — word families explored

The metaphor families this house has already mined, with the semantic map each
one supplies and what it was rejected for. Consult this before brainstorming so
a search never picks back up from a dead family without knowing why.

## The governing idea

A tool name should carry **both** of the tool's halves: the *flow/motion*
(fetch, sync, distribute) and the *record/state* (last-fetch, blocked-since,
lock/pin). Names that carry only one collapse to a single-mechanism image.

## Families

| Family                                                             | Feels like                    | What it supplies                                        | Why it got rejected                                                                             |
| ------------------------------------------------------------------ | ----------------------------- | ------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **canopy / tree-top**                                              | spanning layer over trees     | the collection/overview layer                           | bare `canopy` taken (PyPI + org); tree words taken (`grove`, `orchard`, `willow`, `arbor`)      |
| **water — distribution** (`distributary`, `tributary`)             | flows out to the fleet        | the "manifest out to each machine" story                | `tributary` taken + wrong direction (flows *in*); `distributary` long (no clean 2-letter alias) |
| **tidal** (`tideline`, `tideflow`, `foreshore`, `shoal`)           | ebb/flow cycle, leaves a mark | *both* flow and record; `tideline` = the recorded state | chosen as near-winner; `tideflow` has prior art                                                 |
| **record / ledger** (`repoledger`, `repofolio`, `ledgerline`)      | the standing book             | the lockfile/staleness state                            | `ledger`/`tally`/`recon`/`logbook`/`saga`/`unison` all taken                                    |
| **historian / scribe** (`chronicle`, `codex`, `folio`, `scriven`)  | the story of change           | the "git is the record of change" idea                  | `codex`→OpenAI, `chronicle`/`folio`/`scribe`/`tome`/`vellum`/`palimpsest` taken                 |
| **root / rhizome** (`rhizome`, `radicle`, `radix`, `mycelium`)     | the decentralized network     | the no-master fleet topology                            | `radicle` = a P2P git project, `radix` = Radix UI, `rhizome` taken                              |
| **resonance / sync** (`resonate`, `resonance`, `unison`, `attune`) | in-phase = synced             | the sharpest "sync" meaning                             | all taken by other sync/audio tools                                                             |

## Dead ends to not repeat

- **`git`-substring words**: `agitate`, `cogitate`, `digit`, `legit`, `longitude`,
  `fugitive`, and the `-itis`/demonym words — correct English words, wrong flavor,
  none legible as "manages repos".
- **The `git`/`repo` prefix-mash**: legal but ownability-weak; every serious
  registry name competes with `git`/`repo` tooling.

## The direction gotcha

Water words carry direction, and direction matters: `tributary` flows **in**
(fetch), `distributary` flows **out** (distribute to machines). Name the half the
tool is actually built around. A tool whose headline story is "distribute the
declarative manifest to another machine" wants the outward word, not the inward
one.

## Where this landed

The concrete case that produced this skill: a git repo-fleet manager was named
`redge` (binary) with `redge-cli` (registry namespace), after ~60 words across
these families were checked. The winner came from the registry-name/binary-name
split, not from finding one more unused poem word.
