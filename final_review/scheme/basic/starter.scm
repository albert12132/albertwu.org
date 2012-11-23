
; Q5
(define (filter pred lst)
  ; YOUR CODE HERE
  nil)

; Q5 Tests
(define (less-3 x) (< x 3))

(define (Q5-test) 
  (eq? (filter less-3 (list 1 2 3 4)) '(1 2)))

(define (Q5-test-all)
  (if (not (Q5-test)) "Q5-test failed"
    "Q5 passed!"))

; Q6
(define (interleave list1 list2)
  ; YOUR CODE HERE
  nil)

; Q6 Tests
(define (Q6-test-1)
  (eq? (interleave (list 1 3 5) (list 2 4 6))
       '(1 2 3 4 5 6)))

(define (Q6-test-2)
  (eq? (interleave (list 1 3 5) nil)
       '(1 3 5)))

(define (Q6-test-3)
  (eq? (interleave (list 1 3 5) (list 2 4))
       '(1 2 3 4 5)))

(define (Q6-test-all)
  (cond ((not (Q6-test-1)) "Q6-test-1 fails")
        ((not (Q6-test-2)) "Q6-test-2 fails")
        ((not (Q6-test-3)) "Q6-test-3 fails")
        (else "Q6 passes!")))


; Q7
(define (count-stairways n)
  ; YOUR CODE HERE
  nil)

; Q7 Tests
(define (Q7-test-1)
  (eq? (count-stairways 4) 5))

(define (Q7-test-2)
  (eq? (count-stairways 5) 8))

(define (Q7-test-all)
  (cond ((not (Q7-test-1)) "Q7-test-1 fails")
        ((not (Q7-test-2)) "Q7-test-2 fails")
        (else "Q7 passes!")))
