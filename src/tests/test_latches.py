from py_hardware import SR_latch, Wire

class TestSR_latch:
    def test_SR_latchInputs(self):
        s = Wire()
        r = Wire()
        q = Wire()
        qbar = Wire()

        SR_latch(False, s, r, q, qbar)

        r.value = True

        assert q.value == False
        assert qbar.value == True

        r.value = False

        assert q.value == False
        assert qbar.value == True

        s.value = True

        assert q.value == True
        assert qbar.value == False

        s.value = False

        assert q.value == True
        assert qbar.value == False

        r.value = True

        assert q.value == False
        assert qbar.value == True


        s = Wire()
        r = Wire()
        q = Wire()
        qbar = Wire()

        SR_latch(True, s, r, q, qbar)
        
        r.value = False

        assert q.value == False
        assert qbar.value == True

        r.value = True

        assert q.value == False
        assert qbar.value == True

        s.value = False

        assert q.value == True
        assert qbar.value == False

        s.value = True

        assert q.value == True
        assert qbar.value == False

        r.value = False

        assert q.value == False
        assert qbar.value == True