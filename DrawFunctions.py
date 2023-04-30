import matplotlib.colors as mcolors
from itertools import chain, groupby, zip_longest
from matplotlib import pyplot as plt
from typing import Callable, List, Optional, Tuple

def __group_points_by_cluster(points: List[Tuple], cluster_indices: List[int]) -> List[List[Tuple]]:
    """Takes a list of points and another list with their cluster_indices, groups the points by cluster_indices and
       returns the list of points.

    Args:
        points: The list of points to group.
        cluster_indices: The list of cluster indices for the points. Must reflect the order of `points`.

    Returns:
        A list of clusters, where each cluster is a list of points.
    """
    n = len(points)
    get_point_label = lambda i: cluster_indices[i]
    clusters = groupby(sorted(range(n), key=get_point_label), key=get_point_label)
    return [[points[i] for i in group] for _, group in clusters]

def plot_points(ax, points, color, marker='o'):
    X, Y = zip(*points)
    ax.plot(X, Y, marker=marker, linestyle='none', markersize=8, markerfacecolor=color, markeredgewidth=1, markeredgecolor='k')

def plot_clusters(points, labels, point_markers=[], title='DBSCAN', ax=None):
    if ax is None:
        fig, ax = plt.subplots()
        fig.suptitle(title)
        ax.set_aspect('equal')
        fig.canvas.draw()
    clusters = __group_points_by_cluster(points, labels)
    k = len(clusters)

    if -1 in labels:
        point_markers = ['x'] + point_markers
        colors = ['k'] + list(mcolors.TABLEAU_COLORS.keys())[:k - 1]
    else:
        colors = list(mcolors.TABLEAU_COLORS.keys())[:k]

    point_markers = point_markers[:k]

    for cluster, color, marker in zip_longest(clusters, colors, point_markers, fillvalue='o'):
        plot_points(ax, cluster, color, marker)