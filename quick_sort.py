def quick_sort(lst):
    qs(lst, 0, len(lst)-1)

def qs(lst, first, last):
    # first and last are the range of indexes we want to search for our quicksort
    # if first and last ever "cross" and last is a lower index than first, don't peform any operations
    if first < last:
        # find the splitpoint
        splitpoint = partition(lst, first, last)

        # sort on the left half of the splitpoint
        qs(lst, first, splitpoint-1)

        # sort on the right half of the splitpoint
        qs(lst, splitpoint+1, last)

def partition(lst, first, last):
    # pivot is the value we're going to compare against and later swap into its rightful position in the list, aka the splitpoint
    # however, we can use the first value as the pivot value because we're going to move it into position (splitpoint) at the end
    pivot = lst[first]

    # set the leftmark just right of the pivot value
    leftmark = first+1

    # set the rightmark to the end of the list
    rightmark = last

    # continue this locate & swap as long as the leftmark remains to the left of the rightmark
    while leftmark < rightmark:
        # while our leftmark is still left of the rightmark, increment and check each time if it's higher than the pivot value
        # if it is lower, we can stop incrementing because we found a valid value to swap
        while leftmark <= rightmark and lst[leftmark] <= pivot:
            leftmark += 1
    
        # now perform the same process decrementing the rightmark
        # if the rightmark is still right of the leftmark and the value is higher than the pivot value we can stop because we found a valid swap
        while rightmark >= leftmark and lst[rightmark] >= pivot:
            rightmark -= 1

        # if the marks still have not crossed then we've simply found two values to swap and we should continue with another pairing after the swap
        if leftmark < rightmark:
            lst[leftmark], lst[rightmark] = lst[rightmark], lst[leftmark]

    
    # after we're finished with swapping values on either side of the eventual pivot, it's time to drop the pivot in between the two groupings (splitpoint)
    # we need to use lst[first] on the left to affect the list rather than just changing what the pivot variable points to
    lst[first], lst[rightmark] = lst[rightmark], pivot

    # at this point the rightmark is the splitpoint for future sorts
    return rightmark

def uncrossed(leftmark, rightmark):
    return leftmark < rightmark


lst = [54,26,93,17,77,31,44,55,20]
quick_sort(lst)
print(lst)
