enum BinaryTree<T> {
    Empty,
    Node {
        elem: T,
        left: Box<BinaryTree<T>>,
        right: Box<BinaryTree<T>>,
    },
}

impl<T> BinaryTree<T> {
    pub fn contains(&self, value: &T) -> bool
    where
        T: PartialEq,
    {
        match self {
            BinaryTree::Empty => false,
            BinaryTree::Node { elem, left, right } => {
                elem == value || left.contains(value) || right.contains(value)
            }
        }
    }
}

#[cfg(test)]
mod test {
    use crate::binary_tree::BinaryTree;

    #[test]
    fn test_contains_empty() {
        let tree = BinaryTree::Empty;
        assert_eq!(false, tree.contains(&1))
    }

    #[test]
    fn test_contains() {
        let tree = BinaryTree::Node {
            elem: 2,
            left: Box::new(BinaryTree::Node {
                elem: 1,
                left: Box::new(BinaryTree::Empty),
                right: Box::new(BinaryTree::Empty),
            }),
            right: Box::new(BinaryTree::Node {
                elem: 3,
                left: Box::new(BinaryTree::Empty),
                right: Box::new(BinaryTree::Empty),
            }),
        };
        assert_eq!(true, tree.contains(&1))
    }
}
