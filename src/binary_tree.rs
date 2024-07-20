use std::cmp::Ordering;

#[derive(Debug, PartialEq, Eq)]
struct Node<T: Ord + Clone> {
    elem: T,
    left: Box<BinaryTree<T>>,
    right: Box<BinaryTree<T>>,
}

impl<T: Ord + Clone> Node<T> {
    fn find_max(&self) -> &T {
        let mut subtrees = vec![self];
        let mut max = &self.elem;
        while let Some(subtree) = subtrees.pop() {
            let value = &subtree.elem;
            if value > max {
                max = value;
            }
            if let Some(ref node) = subtree.left.0 {
                subtrees.push(node);
            }
            if let Some(ref node) = subtree.right.0 {
                subtrees.push(node);
            }
        }
        &max
    }
}

#[derive(Debug, PartialEq, Eq)]
struct BinaryTree<T: Ord + Clone>(Option<Node<T>>);

impl<T: Ord + Clone> Default for BinaryTree<T> {
    fn default() -> Self {
        BinaryTree::new()
    }
}

impl<T: Ord + Clone> BinaryTree<T> {
    pub fn new() -> Self {
        BinaryTree(None)
    }

    pub fn contains(&self, value: &T) -> bool
    where
        T: PartialEq,
    {
        match &self.0 {
            Some(Node { elem, left, right }) => {
                elem == value || left.contains(value) || right.contains(value)
            }
            None => false,
        }
    }

    fn values(self) -> Vec<T> {
        let mut subtrees = vec![self];
        let mut values = Vec::new();
        while let Some(subtree) = subtrees.pop() {
            if let Some(Node { elem, left, right }) = subtree.0 {
                values.push(elem);
                subtrees.push(*left);
                subtrees.push(*right);
            }
        }
        return values;
    }

    pub fn insert(&mut self, value: T) {
        match self.0 {
            None => {
                self.0 = Some(Node {
                    elem: value,
                    left: Box::new(BinaryTree(None)),
                    right: Box::new(BinaryTree(None)),
                });
            }
            Some(Node {
                ref elem,
                ref mut left,
                ref mut right,
            }) => match value.cmp(elem) {
                Ordering::Less => left.insert(value),
                Ordering::Equal | Ordering::Greater => right.insert(value),
            },
        }
    }

    pub fn delete(&mut self, value: &T) {
        if let Some(ref mut node) = self.0 {
            match value.cmp(&node.elem) {
                Ordering::Equal => match (&mut *node.left, &mut *node.right) {
                    (BinaryTree(None), BinaryTree(None)) => *self = BinaryTree(None),
                    (BinaryTree(None), node) => self.0 = node.0.take(),
                    (node, BinaryTree(None)) => self.0 = node.0.take(),
                    (BinaryTree(Some(left_node)), _) => {
                        let max_value = left_node.find_max().clone();
                        node.left.delete(&max_value);
                        node.elem = max_value;
                    }
                },
                Ordering::Less => node.left.delete(value),
                Ordering::Greater => node.right.delete(value),
            }
        }
    }
}

impl<T: Ord + Clone> FromIterator<T> for BinaryTree<T>{
    fn from_iter<I: IntoIterator<Item = T>>(iter: I) -> Self {
        let mut tree: BinaryTree<T> = Default::default();
        for elem in iter {
            tree.insert(elem);
        }
        tree
    }
}

#[cfg(test)]
mod test {
    use crate::binary_tree::{BinaryTree, Node};

    #[test]
    fn test_contains_empty() {
        let tree = BinaryTree::new();
        assert_eq!(false, tree.contains(&1))
    }

    #[test]
    fn test_contains() {
        let tree = BinaryTree::from_iter([1, 2, 3]);
        assert_eq!(true, tree.contains(&1))
    }

    #[test]
    fn test_insert() {
        let mut tree = BinaryTree::new();
        tree.insert(2);
        tree.insert(1);
        tree.insert(3);

        let expected = BinaryTree(Some(Node {
            elem: 2,
            left: Box::new(BinaryTree(Some(Node {
                elem: 1,
                left: Box::new(BinaryTree(None)),
                right: Box::new(BinaryTree(None)),
            }))),
            right: Box::new(BinaryTree(Some(Node {
                elem: 3,
                left: Box::new(BinaryTree(None)),
                right: Box::new(BinaryTree(None)),
            }))),
        }));

        assert_eq!(tree, expected);

    }

    #[test]
    fn test_delete_leaf() {
        let mut tree = BinaryTree::from_iter([2, 1, 3]);

        tree.delete(&3);

        let expected = BinaryTree(Some(Node {
            elem: 2,
            left: Box::new(BinaryTree(Some(Node {
                elem: 1,
                left: Box::new(BinaryTree(None)),
                right: Box::new(BinaryTree(None)),
            }))),
            right: Box::new(BinaryTree(None)),
        }));

        assert_eq!(tree, expected);
    }

    #[test]
    fn test_delete_root() {
        let mut tree = BinaryTree::from_iter([2, 1, 3]);

        tree.delete(&2);

        let expected = BinaryTree(Some(Node {
            elem: 1,
            right: Box::new(BinaryTree(Some(Node {
                elem: 3,
                left: Box::new(BinaryTree(None)),
                right: Box::new(BinaryTree(None)),
            }))),
            left: Box::new(BinaryTree(None)),
        }));

        assert_eq!(tree, expected);
    }

    #[test]
    fn test_delete_middle() {
        let mut tree = BinaryTree::from_iter([2, 1, 3, 4]);

        tree.delete(&3);

        let expected = BinaryTree(Some(Node {
            elem: 2,
            left: Box::new(BinaryTree(Some(Node {
                elem: 1,
                left: Box::new(BinaryTree(None)),
                right: Box::new(BinaryTree(None)),
            }))),
            right: Box::new(BinaryTree(Some(Node {
                elem: 4,
                left: Box::new(BinaryTree(None)),
                right: Box::new(BinaryTree(None)),
            }))),
        }));

        assert_eq!(tree, expected);
    }

    #[test]
    fn test_delete_left_max() {
        let mut tree = BinaryTree::from_iter([3, 1, 2, 4]);

        tree.delete(&3);

        let expected = BinaryTree(Some(Node {
            elem: 2,
            left: Box::new(BinaryTree(Some(Node {
                elem: 1,
                left: Box::new(BinaryTree(None)),
                right: Box::new(BinaryTree(None)),
            }))),
            right: Box::new(BinaryTree(Some(Node {
                elem: 4,
                left: Box::new(BinaryTree(None)),
                right: Box::new(BinaryTree(None)),
            }))),
        }));

        assert_eq!(tree, expected);
    }
}
