(define (domain vampire)
    (:requirements :conditional-effects)
    (:predicates
        (light-on ?r)
        (slayer-is-alive)
        (slayer-is-in ?r)
        (vampire-is-alive)
        (vampire-is-in ?r)
        (fighting)
        ;
        ; static predicates
        (NEXT-ROOM ?r ?rn)
        (CONTAINS-GARLIC ?r)
    )

    (:action toggle-light
        :parameters (?anti-clockwise-neighbor ?room ?clockwise-neighbor)
        :precondition (and
            (NEXT-ROOM ?anti-clockwise-neighbor ?room)
            (NEXT-ROOM ?room ?clockwise-neighbor)
            (not (fighting))
        )
        :effect (and
            ;turn on the light in a room where the vampire is
            (when
                ;Antecedence
                (and (not (light-on ?room))
                    (vampire-is-in ?room)
                    (not (light-on ?anti-clockwise-neighbor)))
                ;Consequence
                (and (not (vampire-is-in ?room))
                    (vampire-is-in ?anti-clockwise-neighbor)
                    (light-on ?room)
                    (when 
                        (slayer-is-in ?anti-clockwise-neighbor)
                        (fighting)
                    )
                )
            )
            (when
                ;Antecedence
                (and (not (light-on ?room))
                    (vampire-is-in ?room)
                    (light-on ?anti-clockwise-neighbor))
                ;Consequence
                (and (not (vampire-is-in ?room))
                    (vampire-is-in ?clockwise-neighbor)
                    (light-on ?room)
                    (when 
                        (slayer-is-in ?clockwise-neighbor)
                        (fighting)
                    )
                )
            )

            ;turn off light in a room where the slayer is
            (when
                ;Antecedence
                (and (light-on ?room)
                    (slayer-is-in ?room)
                    (light-on ?clockwise-neighbor))
                ;Consequence
                (and (not (slayer-is-in ?room))
                    (slayer-is-in ?clockwise-neighbor)
                    (not (light-on ?room))
                    (when 
                        (vampire-is-in ?clockwise-neighbor)
                        (fighting)
                    )
                )
            )
            (when
                ;Antecedence
                (and (light-on ?room)
                    (slayer-is-in ?room)
                    (not (light-on ?clockwise-neighbor)))
                ;Consequence
                (and (not (slayer-is-in ?room))
                    (slayer-is-in ?anti-clockwise-neighbor)
                    (not (light-on ?room))
                    (when 
                        (vampire-is-in ?anti-clockwise-neighbor)
                        (fighting)
                    )
                )
            )

            ;when there is no one in the room
            (when 
                ;Antecedence
                (and (not (slayer-is-in ?room))
                    (not (vampire-is-in ?room))
                    (not (light-on ?room)))
                ;Consequence
                (light-on ?room)
            )
            (when 
                ;Antecedence
                (and (not (slayer-is-in ?room))
                    (not (vampire-is-in ?room))
                    (light-on ?room))
                ;Consequence
                (not (light-on ?room))
            )
        )
    )

    (:action watch-fight
        :parameters (?room)
        :precondition (and
            (slayer-is-in ?room)
            (slayer-is-alive)
            (vampire-is-in ?room)
            (vampire-is-alive)
            (fighting)
        )
        :effect (and
            (when
                (light-on ?room)
                (and (not (vampire-is-alive))
                    (not (fighting)))
            )

            (when
                (and (not (light-on ?room))
                    (CONTAINS-GARLIC ?room))
                (and (not (vampire-is-alive))
                    (not (fighting)))
            )

            (when
                (and (not (light-on ?room))
                    (not (CONTAINS-GARLIC ?room)))
                (and (not (slayer-is-alive))
                    (not (fighting)))
            )
        )
    )
)
