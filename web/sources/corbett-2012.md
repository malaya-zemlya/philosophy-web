---
id: source-corbett-2012
type: source
title: Corbett et al. — Spanner, Google's globally-distributed database (2012)
author: mishka
status: asserted
tags: [distributed-systems, computer-science, time]
created: 2026-11-21
---

relevance (content): the paper describing Spanner, the first database to give externally consistent
transactions at global scale. It does so by engineering a bound on clock uncertainty (the TrueTime
API, backed by GPS and atomic clocks) and making each commit wait out that uncertainty. It is the
model case of global consistency bought at a cost in hardware and latency, the analogy at the centre
of [distributed-brain-unity](../arguments/distributed-brain-unity.md).

Reference:
- Corbett, J. C., Dean, J., Epstein, M., Fikes, A., Frost, C., Furman, J. J., Ghemawat, S., Gubarev,
  A., Heiser, C., Hochschild, P., Hsieh, W., Kanthak, S., Kogan, E., Li, H., Lloyd, A., Melnik, S.,
  Mwaura, D., Nagle, D., Quinlan, S., … Woodford, D. (2012). Spanner: Google's globally-distributed
  database. In *Proceedings of the 10th USENIX Symposium on Operating Systems Design and
  Implementation (OSDI '12)* (pp. 251–264). USENIX Association.
  https://www.usenix.org/conference/osdi12/technical-sessions/presentation/corbett
