<?php
$active = FLASE;

if($active){
    # upload files
    $nid = $node->nid;
    $uploads = array();
    foreach ($files as $file){
        $upl = new StdClass();
        $upl->fid = 'upload';
        $upl->filename = $file['dest_path'];
        $upl->filepath = $file['src_path'];
        $upload->filemime = 'image/jpeg';
        $upl->filesize = $file['size'];
        //$upl->description = $file[1];
        $upl->list = 1;
        array_push($uploads, $upl);
    }
   
    $node->files = $uploads;
    upload_save($node);
   
    # save image fields
    $files = $node->files;
    $images = array();
    foreach($files as $file){
        array_push($images,array(
                'title' => $file->filename,
                'nid' => $nid,
                'fid' => $file->fid
            )
        );
    }
    $node->field_diaporama = $images;
    node_save($node);
}
?>