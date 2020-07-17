package p100to199

import "testing"

func Test_isPalindrome(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		// Case 1
		{
			name: "Case 1",
			args: args{s: "A man, a plan, a canal: Panama"},
			want: true,
		},
		// Case 2
		{
			name: "Case 2",
			args: args{s: "race a car"},
			want: false,
		},
		// Case 3
		{
			name: "Case 3",
			args: args{s: ".,"},
			want: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isPalindrome(tt.args.s); got != tt.want {
				t.Errorf("isPalindrome() = %v, want %v", got, tt.want)
			}
		})
	}
}
