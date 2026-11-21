---
id: claim-distributed-consistency-is-costly
type: claim
title: In a distributed system with significant signal delays, a globally consistent state does not arise by default but must be engineered at a cost
headword: Costly distributed consistency
author: generic
status: asserted
tags: [distributed-systems, computer-science, time]
style: encyclopedia
created: 2026-11-21
---

When separate processes communicate only by messages that take time to arrive, the system has no
shared "now". Each process has its own view, and events at different processes are only partially
ordered by what could have caused what ([lamport-1978](../sources/lamport-1978.md)). A single consistent state of the
whole system has to be constructed by a protocol, and the protocol costs something: extra messages,
synchronised clocks, or waiting. Google's Spanner database achieves global consistency only by
bounding clock uncertainty with GPS and atomic clocks and making each transaction wait out that
uncertainty before it commits ([corbett-2012](../sources/corbett-2012.md)). When the network is cut, the system must
give up either consistency or availability (the CAP theorem; [gilbert-lynch-2002](../sources/gilbert-lynch-2002.md)).

### Scope

The claim is a general result of computer science about systems of communicating processes. It does
not say what any particular system, such as a brain, actually does.

### In plain terms

When many computers work together but their messages take time to arrive, they never automatically
agree on what is happening right now. Getting them to agree takes special machinery and costs time,
and if the connection between them breaks they have to choose between agreeing and continuing to work.
