class Node {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class BST {
    constructor() {
        this.root = null;
    }
    add(value) {
        if (this.root == null) {
            this.root = new Node(value);
            return this;
        }
        let runner = this.root;
        while (runner !== null) {
            if (value < runner.value) {
                if (runner.left == null) {
                    runner.left = new Node(value);
                    return this;
                }
                // if the runner.left postion is already filled.
                runner = runner.left;
            }
            else {
                if (runner.right == null) {
                    runner.right = new Node(value);
                    return this;
                }
                runner = runner.right;
            }
        }
    }
    contains(value) {
        if (this.root == null) {
            return false;
        }
        let runner = this.root;
        while (runner !== null) {
            if (value == runner.value) {
                return true;
            }
            else if (value < runner.value) {
                runner = runner.left;
            }
            else {
                runner = runner.right;
            }
        }
        return false;
    }
    isEmpty() {
        if (this.root) {
            return false;
        }
        else {
            return true;
        }
    }
    size() {
        if (this.root == null) {
            return 0; // empty tree, 0 nodes
        }
        function helper(runner) {
            if (runner == null) {
                return 0
            }
            // Return 1 is head postion + recursive runner.left + recursive runner.right
            return 1 + helper(runner.left) + helper(runner.right)
        }
        return helper(this.root)
    }
    max() {
        let runner = this.root;
        let max = this.root.value;
        if (runner == null) {
            return "You have nothing"
        }
        while (runner.right) {
            if (runner.right.value > max) {
                max = runner.right.value;
            }
            runner = runner.right;
        }
        return max;
    }
    min() {
        let runner = this.root;
        let min = this.root.value;
        if (runner == null) {
            return "You have nothing"
        }
        while (runner.left) {
            if (runner.left.value < min) {
                min = runner.left.value;
            }
            runner = runner.left;
        }
        return min;
    }
    height(root) {
        // empty tree has height -1
        if (this.root == null) {
            return -1;
        }
        return Math.max(this.height(root.left) + this.height(root.right)) + 1


    }
    isBalanced(runner) {
        if (this.root == null) { // base case
            return 0;
        }
        var runner = this.root;
        var leftHeight = isBalanced(runner.left);
        var rightHeight = isBalanced(runner.right);

        // In case tree is unbalanced
        if (Math.abs(leftHeight - rightHeight) > 1) {
            return false
        }
        else {
            return Math.max(leftHeight, rightHeight) + 1;
        }
    }
}


myTree = new BST();
console.log(myTree.add(30).add(10).add(40).add(20));
console.log(myTree.contains(56))
console.log(myTree.height())
console.log(myTree.isBalanced())