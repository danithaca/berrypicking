/**
 * Sample input:
 *
 *          1
 *         / \
 *        3   5
 *       /   / \
 *      2   4   7
 *     / \   \
 *    9   6   8
 
 *
 * Expected output:
 *    1
 *    3 5
 *    2 4 7
 *    9 6 8
 *    ==========
 */
class TreePrinter {
 
  static class Node {
    int value;
    Node left;
    Node right;
    public Node(int value, Node left, Node right) {
      this.value = value;
      this.left = left;
      this.right = right;
    }
  }
 
  public void printTree(Node root) {
    // implementation here
  }
}

# python code starts here

# use a list to save the traverse path
# use None to mark the end of one level

def print_tree(root): # 1
  lst = []
  lst.append(root) # [1]
  lst.append(None) # [1, None]
  
  # traverse here
  iter = lst.iterator()
  while(iter.hasNext()):
    node = iter.next() # 1, None, 3, 
    # print a new line if end of level
    if node is None:
      print("\n") # 1\n
      lst.append(None) # [3, 5, None]
    else:
      print(node.value) # 1, 3
      if node.left is not None: lst.append(node.left) # [None, 3], [5, None, 2]
      if node.right is not None: lst.append(node.right) # [None, 3, 5]
      



/* This class will be given a list of words (such as might be tokenized
 * from a paragraph of text), and will provide a method that takes two
 * words and returns the shortest distance (in words) between those two
 * words in the provided text.
 * Example:
 *   WordDistanceFinder finder = new WordDistanceFinder(Arrays.asList("the", "quick", "brown", "fox", "quick"));
 *   assert(finder.distance("fox","the") == 3);
 *   assert(finder.distance("quick", "fox") == 1);
 *
 * "quick" appears twice in the input. There are two possible distance values for "quick" and "fox":
 *     (3 - 1) = 2 and (4 - 3) = 1.
 * Since we have to return the shortest distance between the two words we return 1.
 */
public class WordDistanceFinder {
    public WordDistanceFinder (List<String> words) {
        // implementation here
    }
    public int distance (String wordOne, String wordTwo) {
        // implementation here
    }
}

