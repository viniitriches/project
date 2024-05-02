(define (domain wumpus-domain)
  (:requirements :strips :typing :negative-preconditions)

  (:functions
  (total-cost)
   )
  
  (:types
    agent
    cell
    item
   )

  (:predicates
    (at ?what ?cell)
    (is-adj ?cell1 ?cell2)
    (is-agent ?who)
    (gold-at ?what)
    (wumpus-at ?square)
    (pit-at ?square)
    (exit-at ?square)
    (have ?who ?what)
    (dead ?who)
    (did-climb)
   )
  
  (:action climb
    :parameters (?who ?square)
    :precondition (and (is-agent ?who)
                       (at ?who ?square)
                       (exit-at ?square))
    :effect (and (not (at ?who ?square))
                 (did-climb)
                 (increase (total-cost) 1))
   )

  (:action grab
    :parameters (?who ?gold ?square)
    :precondition (and (is-agent ?who)
                       (at ?who ?square)
                       (gold-at ?square))
    :effect (and (have ?who ?gold)
                 (not (gold-at ?square))
                 (increase (total-cost) 1))
   )

  (:action move
    :parameters (?who ?cell ?new-cell)
    :precondition (and (is-agent ?who)
                       (at ?who ?cell)
                       (is-adj ?cell ?new-cell)
                       (not (pit-at ?new-cell))
                       (not (wumpus-at ?new-cell)))
    :effect (and (not (at ?who ?cell))
                 (at ?who ?new-cell)
                 (increase (total-cost) 1))
   )

  (:action shoot
  :parameters (?arrow ?who ?cell1 ?wumpus ?cell2)
  :precondition (and (is-agent ?who)
                     (at ?who ?square)
                     (have ?who ?arrow)
                     (wumpus-at ?cell)
                     (adj ?cell1 ?cell2))
  :effect (and (dead ?wumpus)
               (not (wumpus-at ?cell2))
               (not (have ?who ?arrow))
               (increase (total-cost) 10))
   )
)