use std::cmp::Ordering;

#[derive(Debug, PartialEq, Eq)]
struct Node<T: Ord + Clone> {
    elem: T,
    left: Option<Box<Node<T>>>,
    right: Option<Box<Node<T>>>,
}

impl<T: Ord + Clone> Node<T> {
    fn leaf(elem: T) -> Node<T> {
        Node {
            elem,
            left: None,
            right: None,
        }
    }

    fn find_max(&self) -> &T {
        let mut subtrees = vec![self];
        let mut max = &self.elem;
        while let Some(subtree) = subtrees.pop() {
            let value = &subtree.elem;
            if value > max {
                max = value;
            }
            if let Some(ref node) = subtree.left {
                subtrees.push(node);
            }
            if let Some(ref node) = subtree.right {
                subtrees.push(node);
            }
        }
        &max
    }

    fn contains(&self, value: &T) -> bool
    where
        T: PartialEq,
    {
        &self.elem == value
            || self.left.as_ref().is_some_and(|left| left.contains(value))
            || self
                .right
                .as_ref()
                .is_some_and(|right| right.contains(value))
    }

    fn insert(&mut self, value: T) {
        let node_to_add = match value.cmp(&self.elem) {
            Ordering::Less => &mut self.left,
            Ordering::Greater | Ordering::Equal => &mut self.right,
        };
        match node_to_add {
            Some(node) => {
                node.insert(value);
            }
            None => {
                self.right = Some(Box::new(Node::leaf(value)));
            }
        }
    }

    fn delete(&self, value: &T) {
        match value.cmp(&self.elem) {
            Ordering::Equal => match (self.left, self.right) {
                (None, None) => self = None,
                (None, node) => self = node.0.take(),
                (node, None) => self = node.0.take(),
                (Some(left_node), _) => {
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
        self.0.as_ref().is_some_and(|node| node.contains(value))
    }

    pub fn insert(&mut self, value: T) {
        match self.0 {
            None => {
                self.0 = Some(Node {
                    elem: value,
                    left: None,
                    right: None,
                });
            }
            Some(ref mut node) => node.insert(value),
        }
    }

    pub fn delete(&mut self, value: &T) {
        if let Some(ref mut node) = self.0 {
            node.delete(value);
        }
    }
}

impl<T: Ord + Clone> FromIterator<T> for BinaryTree<T> {
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
