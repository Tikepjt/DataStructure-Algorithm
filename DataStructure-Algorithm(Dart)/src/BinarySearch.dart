int BinarySearch(List<int> list, int item) {
  int low = 0;
  int high = list.length - 1;

  while (low <= high) {
    int mid = ((low + high) / 2).floor();
    int guess = list[mid];
    print("$low,$high,$mid,$guess");
    if (guess == item) {
      return mid;
    } else if (guess > item) {
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }

  return 0;
}

void main() {
  var myList = new List<int>();
  myList.add([1, 3, 5, 7, 9]);
  print("${BinarySearch(myList, 3)}");
  print("${BinarySearch(myList, -1)}");
}
