const plusOne = function (digits) {
	let numDigits = BigInt(digits.join(""));
	numDigits++;
	digits = String(numDigits).split("");
	return digits;
};
