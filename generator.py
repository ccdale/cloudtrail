def aFunc():
    try:
        al = [1, 2, 3, 4]
        for x in al:
            yield x
    except StopIteration:
        print("aFunc: we've fallen off the end of the list")
    except Exception as e:
        print(f"aFunc: another exception occurred: {e}")


if __name__ == "__main__":
    try:
        for y in aFunc():
            print(y)
    except Exception as e:
        print(f"main exception occurred: {e}")
