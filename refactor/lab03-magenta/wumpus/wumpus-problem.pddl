(define (problem wumpus-problem)
  (:domain wumpus-domain)
  
(:requirements :action-costs)
  
(:objects
    agent
    arrow
    sq-0-0
    sq-0-1
    sq-0-2
    sq-0-3
    sq-1-0
    sq-1-1
    sq-1-2
    sq-1-3
    sq-2-0
    sq-2-1
    wumpus
    pit
    sq-2-2
    sq-2-3
    gold
    sq-3-0
    sq-3-1
    sq-3-2
    sq-3-3
  )
  (:init
    (at agent sq-0-0)
    (at gold sq-3-0)
    (at wumpus sq-2-2)
    (at pit sq-2-2)
    (arrow-is arrow)
    (agent-is agent)
    (takeable gold)
    (have agent arrow)
    (exit-is sq-0-0)
    (= (total-cost) 0)
    (adj sq-0-0 sq-0-1)
    (adj sq-0-0 sq-1-0)
    (adj sq-0-1 sq-0-2)
    (adj sq-0-1 sq-0-0)
    (adj sq-0-1 sq-1-1)
    (adj sq-0-2 sq-0-3)
    (adj sq-0-2 sq-0-1)
    (adj sq-0-2 sq-1-2)
    (adj sq-0-3 sq-0-2)
    (adj sq-0-3 sq-1-3)
    (adj sq-1-0 sq-1-1)
    (adj sq-1-0 sq-2-0)
    (adj sq-1-0 sq-0-0)
    (adj sq-1-1 sq-1-2)
    (adj sq-1-1 sq-1-0)
    (adj sq-1-1 sq-2-1)
    (adj sq-1-1 sq-0-1)
    (adj sq-1-2 sq-1-3)
    (adj sq-1-2 sq-1-1)
    (adj sq-1-2 sq-2-2)
    (adj sq-1-2 sq-0-2)
    (adj sq-1-3 sq-1-2)
    (adj sq-1-3 sq-2-3)
    (adj sq-1-3 sq-0-3)
    (adj sq-2-0 sq-2-1)
    (adj sq-2-0 sq-3-0)
    (adj sq-2-0 sq-1-0)
    (adj sq-2-1 sq-2-2)
    (adj sq-2-1 sq-2-0)
    (adj sq-2-1 sq-3-1)
    (adj sq-2-1 sq-1-1)
    (wumpus-is wumpus)
    (pit-is pit)
    (adj sq-2-2 sq-2-3)
    (adj sq-2-2 sq-2-1)
    (adj sq-2-2 sq-3-2)
    (adj sq-2-2 sq-1-2)
    (adj sq-2-3 sq-2-2)
    (adj sq-2-3 sq-3-3)
    (adj sq-2-3 sq-1-3)
    (gold-is gold)
    (adj sq-3-0 sq-3-1)
    (adj sq-3-0 sq-2-0)
    (adj sq-3-1 sq-3-2)
    (adj sq-3-1 sq-3-0)
    (adj sq-3-1 sq-2-1)
    (adj sq-3-2 sq-3-3)
    (adj sq-3-2 sq-3-1)
    (adj sq-3-2 sq-2-2)
    (adj sq-3-3 sq-3-2)
    (adj sq-3-3 sq-2-3)
  )
  (:goal
    (and (have agent gold) (did-climb)))
  
(:metric minimize (total-cost))
)
