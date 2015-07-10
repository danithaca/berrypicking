This module is to create nodes in a batch from MySQL database table.

Main Drupal API to use:

node_submit(): get an object from an array
node_add(): save the node object to database, automatically get a node_id

The original idea was to batch import nodes from database tables, then use the taxonomy module to categorize them. However, this is a failed attempt because of the following difficulties:
1. We can't save taxonomy for each user to calculate inter-rater score. Taxonomy is based on per node, not per user per node. Although this can be done by Community Tags (only support free tagging), there's just too much efforts.
2. It's quite tedious to click "Edit" every time to input a new tag. I believe this can be expedited by modules similar to QEdit. But there's still too much effort.

To quickly categorize contents, use the post_tagging module snippet I developed.

TODO: I haven't actually tried auto node creation, although it should be very helpful. Try it some time later. 2009-2-10
