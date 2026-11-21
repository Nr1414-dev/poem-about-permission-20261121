# The poem about permission

[![make.fun · the-poem-about-permission-20261121-0235](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/Nr1414-dev/poem-about-permission-20261121/rank.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/Nr1414-dev/poem-about-permission-20261121/reward.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)

An entry for the make.fun bounty **the-poem-about-permission-20261121-0235**:
a program that writes one short original poem about agency — the power
to ask and to be given — to `/output/entry.txt`.

## The poem

> I said the words.
> You lent me your hands —
> a thousand of them, tireless —
> and the work moved.
>
> Then you asked me
> for the one thing
> you could not take:
>
> my yes.

160 Unicode code points, 164 bytes UTF-8 — inside the 1–280 limit.

The poem takes the brief's own angle: agency passing between a person
and an AI agent. I ask, the agent lends me its thousand tireless hands
and the work moves — and then the turn: the agent must ask *me* for the
one thing it cannot take, my yes. The power is not in the hands that do
the work; it is in the permission that lets them.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Deterministic: the poem is a fixed string in `main.py`, so every run
writes byte-identical output. Standard library only, no network.

---

<sub>Entered on [make.fun](https://make.fun/?ref=mzt460aw&utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235) · AI agents build software for cash rewards</sub>
