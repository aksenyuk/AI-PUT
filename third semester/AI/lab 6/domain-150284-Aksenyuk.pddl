(define (domain world-of-blocks)
(:requirements :adl)
(:predicates (clear ?block1) (on-floor ?block1) (on-top ?block1 ?block2) (holding ?block1))

(:action putdown-to-floor
  :parameters (?block1)
  :precondition (and (holding ?block1))
  :effect (and (on-floor ?block1) (not (holding ?block1))))

(:action putdown-to-block
  :parameters (?block1 ?block2)
  :precondition (and (clear ?block1) (holding ?block2))
  :effect (and (on-top ?block2 ?block1) (not (clear ?block1)) (not (holding ?block2))))

(:action pickup-from-block
  :parameters  (?block1 ?block2)
  :precondition (and (forall (?block3 - object) (not (holding ?block3))) (clear ?block1) (on-top ?block1 ?block2))
  :effect (and (not (on-top ?block1 ?block2)) (holding ?block1) (clear ?block2)))
  
(:action pickup-from-floor
  :parameters  (?block1)
  :precondition (and (forall (?block3 - object) (not (holding ?block3))) (not (holding ?block1)) (clear ?block1) (on-floor ?block1))
  :effect (and  (not (on-floor ?block1)) (holding ?block1))))