---
id: source-lamport-1978
type: source
title: Lamport — Time, clocks, and the ordering of events in a distributed system (1978)
author: mishka
status: asserted
tags: [distributed-systems, computer-science, time]
created: 2026-11-21
---

relevance (content): the founding paper on time in distributed systems. It shows that "happened
before" is only a partial order among events at separate, communicating processes, so a system of
such processes has no global order of events, and no shared "now", unless one is constructed by a
synchronisation algorithm. Grounds [distributed-consistency-is-costly](../claims/distributed-consistency-is-costly.md).

Reference:
- Lamport, L. (1978). Time, clocks, and the ordering of events in a distributed system.
  *Communications of the ACM, 21*(7), 558–565. https://doi.org/10.1145/359545.359563
