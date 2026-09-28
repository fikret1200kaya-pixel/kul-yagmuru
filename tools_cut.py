import cv2, numpy as np
from PIL import Image
def cut_cells(path, rows, cols, out, thr=40, keep_ratio=0.02, cells=None, bigbg=0):
    im=np.array(Image.open(path).convert('RGB')).astype(np.int16)
    H,W,_=im.shape
    paper=np.median(np.concatenate([im[:8].reshape(-1,3),im[-8:].reshape(-1,3)]),axis=0)
    k=0
    for r in range(rows):
        for c in range(cols):
            k+=1
            if cells and k not in cells: continue
            y0,y1=r*H//rows,(r+1)*H//rows; x0,x1=c*W//cols,(c+1)*W//cols
            sub=im[y0:y1,x0:x1]
            d=np.abs(sub-paper).sum(2)
            cand=(d<=thr).astype(np.uint8)
            n0,l0,_,_=cv2.connectedComponentsWithStats(cand)
            border=set(np.unique(np.concatenate([l0[0],l0[-1],l0[:,0],l0[:,-1]])))-{0}
            bgm=np.isin(l0,list(border))
            if bigbg:
                n1,l1,s1,_=cv2.connectedComponentsWithStats(cand)
                bigs=[i for i in range(1,n1) if s1[i,4]>bigbg]
                bgm|=np.isin(l1,bigs)
            fg=(~bgm).astype(np.uint8)
            fg=cv2.morphologyEx(fg,cv2.MORPH_OPEN,np.ones((2,2),np.uint8))
            fg=cv2.morphologyEx(fg,cv2.MORPH_CLOSE,np.ones((5,5),np.uint8))
            n,lab,st,_=cv2.connectedComponentsWithStats(fg)
            if n<2: continue
            big=st[1:,4].max()
            keep=np.zeros_like(fg)
            bi=1+int(np.argmax(st[1:,4])); W2=fg.shape[1]
            for i in range(1,n):
                x,y,bw,bh,ar=st[i]
                edge=(x<=1 or x+bw>=W2-1)
                if i!=bi and edge: continue
                if ar>=big*keep_ratio: keep[lab==i]=1
            # fill holes
            h,w=keep.shape
            if bigbg: inv=None
            if not bigbg:
              inv=((1-keep)*255).astype(np.uint8); m=np.zeros((h+2,w+2),np.uint8)
            pass
            if not bigbg:
              cv2.floodFill(inv,m,(0,0),0); keep=np.maximum(keep,(inv>0).astype(np.uint8))
            a=cv2.GaussianBlur(keep.astype(np.float32),(3,3),0)
            ys,xs=np.where(keep>0); by0,by1,bx0,bx1=ys.min(),ys.max()+1,xs.min(),xs.max()+1
            rgba=np.dstack([sub.astype(np.uint8),(a*255).astype(np.uint8)])[by0:by1,bx0:bx1]
            Image.fromarray(rgba).save(f'assets/proc/{out}_{k}.png')
            print(out,k,rgba.shape)
if __name__=='__main__':
    cut_cells('assets/raw/lehim_karakter_sayfasi.webp',2,3,'lehim')
    cut_cells('assets/raw/C1_son_bahcivan.png',1,4,'bahcivan',thr=75,bigbg=300,keep_ratio=0.0015)
