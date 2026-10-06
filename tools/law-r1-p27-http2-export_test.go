package http2

func (sc *serverConn) TestPushEnabled() bool {
	ch := make(chan bool, 1)
	sc.serveMsgCh <- func(int) {
		ch <- sc.pushEnabled
	}
	return <-ch
}
