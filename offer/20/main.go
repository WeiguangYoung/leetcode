package main

type State int
type CharType int

const (
    STATE_INITIAL State = iota
    STATE_INT_SIGN
    STATE_INTEGER
    STATE_POINT
    STATE_POINT_WITHOUT_INT
    STATE_FRACTION
    STATE_EXP
    STATE_EXP_SIGN
    STATE_EXP_NUMBER
    STATE_END
)

const (
    CHAR_NUMBER CharType = iota
    CHAR_EXP
    CHAR_POINT
    CHAR_SIGN
    CHAR_SPACE
    CHAR_ILLEGAL
)

func toCharType(ch byte) CharType {
    switch ch {
    case '0', '1', '2', '3', '4', '5', '6', '7', '8', '9':
        return CHAR_NUMBER
    case 'e', 'E':
        return CHAR_EXP
    case '.':
        return CHAR_POINT
    case '+', '-':
        return CHAR_SIGN
    case ' ':
        return CHAR_SPACE
    default:
        return CHAR_ILLEGAL
    }
}

// ` sd.sded `
func isNumber(s string) bool {
	// tansfer := map[State]map[CharType]State{
	// 	STATE_INITIAL: map[CharType]State{
	// 		CHAR_SPACE: STATE_INITIAL,
	// 		CHAR_SIGN: STATE_INT_SIGN,
	// 		CHAR_NUMBER: STATE_INTEGER,
	// 	},
	// }
	return false
}
