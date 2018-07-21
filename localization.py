from matplotlib import patches, patheffects
import numpy as np


def bb_hw(a):
    """Converts Bounding Box from x1,y1,x2,y2
    to VOC style x,y,l,b 
    """
    return np.array([a[1]a[0],a[3]-a[1]+1,a[2],a[0]+1])

def hw_bb(bb): 
    """Converts x,y,l,b to x,y,x,y
    i.e. Converts VOC style bounding box to x1,y1,x2,y2
    """
    return np.array([bb[1], bb[0], bb[3]+bb[1]-1, bb[2]+bb[0]-1])

def show_img(im, figsize,=None, ax=None):
    """Plot Image and return axis
    You can also pass an exis to plot on."""
    if not ax: fig,ax = plt.subplots(figsize=figsize)
    ax.imshow(im)
    ax.get_xaxis().set_vissible(False)
    ax.get_yaxis().set_vissible(False)
    return ax

def draw_outline(o,lw):
    o.set_path_effects(
        [patheffects.Stroke(linewidth=lw, 
        foreground='black'), 
        patheffects.Normal()])

def draw_rect(ax, b):
    patch = ax.add_patch(patches.Rectangle(b[:2], *b[-2:], fill=False, edgecolor='white', lw=2))
    draw_outline(patch, 4)

def draw_text(ax, xy, txt, sz=14):
    text = ax.text(*xy, txt,
        verticalalignment='top', color='white', fontsize=sz, weight='bold')
    draw_outline(text, 1)

def draw_im(im, ann):
    """Draw Image with annotations
    im:  image to draw
    ann: annotations as list of [bbox, categ]
         bbox as x1,y1,x2,y2
         categ as text to write on top.
    """
    ax = show_img(im, figsize=(16,8))
    for b,c in ann:
        b = bb_hw(b)
        draw_rect(ax, b)
        draw_text(ax, b[:2], cats[c], sz=16)

